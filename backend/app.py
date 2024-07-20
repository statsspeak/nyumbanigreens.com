from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from flask import send_from_directory
import pymysql
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'kwetu'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')


# Initialize pymysql connection
db = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB'],
    cursorclass=pymysql.cursors.DictCursor
)

# Ensure the UPLOAD_FOLDER directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


def get_shop_by_id(shop_id):
    with pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    ) as db:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM shops WHERE id = %s", (shop_id,))
            shop = cursor.fetchone()
    return shop



@app.route('/')
def clients_page():
    try:
        with db.cursor() as cursor:
            # Read all shops from the database
            cursor.execute('SELECT * FROM shops')
            shops = cursor.fetchall()

            # Get the file names for the shop images
            for shop in shops:
                if shop['shop_image']:
                    shop['shop_image'] = os.path.basename(shop['shop_image'])
                else:
                    shop['shop_image'] = 'placeholder.jpg'

            return render_template('clients_page.html', shops=shops)
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        return "Error connecting to MySQL"


@app.route('/view_shop/<int:shop_id>')
def view_shop(shop_id):
    try:
        with db.cursor() as cursor:
            # Fetch the shop details
            sql = "SELECT * FROM shops WHERE id = %s"
            cursor.execute(sql, (shop_id,))
            shop = cursor.fetchone()

            # Fetch the items for the shop
            sql = "SELECT * FROM items WHERE shop_id = %s AND available = 1"
            cursor.execute(sql, (shop_id,))
            items = cursor.fetchall()

            # Group the items by category
            items_by_category = {}
            for item in items:
                category = item['category']
                if category not in items_by_category:
                    items_by_category[category] = []
                items_by_category[category].append(item)

        if shop:
            return render_template('view_shop.html', shop=shop, items_by_category=items_by_category, os=os)
        else:
            return 'Shop not found', 404
    except pymysql.Error as e:
        print(f"Error fetching shop and items: {e}")
        return 'Error fetching shop and items', 500



# Example route to display shop dashboard and management links
@app.route('/shop_dashboard/<int:shop_id>')
def shop_dashboard(shop_id):
    try:
        # Fetch shop name from database using pymysql
        with db.cursor() as cursor:
            sql = "SELECT shop_name FROM shops WHERE id = %s"
            cursor.execute(sql, (shop_id,))
            shop = cursor.fetchone()

        if shop:
            shop_name = shop['shop_name']
            return render_template('shop_dashboard.html', shop_id=shop_id, shop_name=shop_name)
        else:
            return "Shop not found"

    except pymysql.Error as e:
        print(f"Error fetching shop details: {e}")
        return "Error fetching shop details"

@app.route('/shop_details/<int:shop_id>')
def shop_details(shop_id):
    try:
        with db.cursor() as cursor:
            sql = "SELECT * FROM shops WHERE id = %s"
            cursor.execute(sql, (shop_id,))
            shop = cursor.fetchone()

        return render_template('shop_details.html', shop=shop, previous_page=request.referrer)
    except pymysql.Error as e:
        print(f"Error fetching shop details: {e}")
        return "Error fetching shop details"



# Route to serve uploaded files (images)
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/item_management/<int:shop_id>', methods=['GET', 'POST'])
def item_management(shop_id):
    if request.method == 'POST':
        try:
            # Retrieve form data
            item_name = request.form.get('item_name')
            description = request.form.get('description')
            price = request.form.get('price')
            category = request.form.get('category')
            image = request.files.get('image')

            # Validate form data (basic validation)
            if not all([item_name, description, price, category, image]):
                flash('Please fill in all fields', 'error')
                return redirect(url_for('item_management', shop_id=shop_id))

            # Save item to database
            try:
                # Connect to the database
                db = pymysql.connect(
                    host=app.config['MYSQL_HOST'],
                    user=app.config['MYSQL_USER'],
                    password=app.config['MYSQL_PASSWORD'],
                    db=app.config['MYSQL_DB'],
                    cursorclass=pymysql.cursors.DictCursor
                )

                with db.cursor() as cursor:
                    # Insert item into 'items' table
                    sql = "INSERT INTO items (item_name, description, price, category, image_filename, shop_id) VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, (item_name, description, price, category, image.filename, shop_id))
                    db.commit()

                    # Handle file upload if needed
                    if image:
                        filename = secure_filename(image.filename)
                        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                    flash('Item registered successfully', 'success')
                    return redirect(url_for('item_management', shop_id=shop_id))

            except Exception as e:
                flash(f'An error occurred while inserting into database: {str(e)}', 'error')
                return redirect(url_for('item_management', shop_id=shop_id))

            finally:
                db.close()

        except Exception as e:
            flash(f'Form submission error: {str(e)}', 'error')
            return redirect(url_for('item_management', shop_id=shop_id))

    # Fetch items from the database for the current shop_id
    try:
        db = pymysql.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DB'],
            cursorclass=pymysql.cursors.DictCursor
        )

        with db.cursor() as cursor:
            # Select items for the current shop_id
            sql = "SELECT * FROM items WHERE shop_id = %s"
            cursor.execute(sql, (shop_id,))
            items = cursor.fetchall()

    except Exception as e:
        flash(f'Error fetching items: {str(e)}', 'error')
        items = []

    finally:
        db.close()

    # Render the item management page with shop_id and items fetched
    return render_template('item_management.html', shop_id=shop_id, items=items)



# Route to edit item details
@app.route('/edit_item/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    if request.method == 'POST':
        item_name = request.form['item_name']
        description = request.form['description']
        price = request.form['price']
        category = request.form['category']
        available = True if request.form.get('available') == 'on' else False

        try:
            # Update item in database
            cursor = db.cursor()
            sql = "UPDATE items SET item_name=%s, description=%s, price=%s, category=%s, available=%s WHERE id=%s"
            cursor.execute(sql, (item_name, description, price, category, available, item_id))
            db.commit()
            flash('Item updated successfully!', 'success')
        except Exception as e:
            print(f"Error updating item: {str(e)}")
            db.rollback()
            flash('Failed to update item. Please try again.', 'error')

        return redirect(url_for('item_management', shop_id=1))  # Replace 1 with actual shop_id

    try:
        # Fetch item details for editing
        cursor = db.cursor()
        sql = "SELECT * FROM items WHERE id = %s"
        cursor.execute(sql, (item_id,))
        item = cursor.fetchone()
        return render_template('edit_item.html', item=item)
    except Exception as e:
        print(f"Error fetching item details: {str(e)}")
        return "Error fetching item details from database"

# Route to delete item
@app.route('/delete_item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    try:
        # Delete item from database
        cursor = db.cursor()
        sql = "DELETE FROM items WHERE id = %s"
        cursor.execute(sql, (item_id,))
        db.commit()
        flash('Item deleted successfully!', 'success')
    except Exception as e:
        print(f"Error deleting item: {str(e)}")
        db.rollback()
        flash('Failed to delete item. Please try again.', 'error')

    return redirect(url_for('item_management', shop_id=1))  # Replace 1 with actual shop_id

# Route to toggle item availability
@app.route('/toggle_availability/<int:item_id>', methods=['POST'])
def toggle_availability(item_id):
    try:
        # Fetch current availability status
        cursor = db.cursor()
        sql_select = "SELECT available FROM items WHERE id = %s"
        cursor.execute(sql_select, (item_id,))
        result = cursor.fetchone()

        if result:
            current_availability = result['available']
            new_availability = not current_availability  # Toggle availability

            # Update availability in database
            sql_update = "UPDATE items SET available=%s WHERE id=%s"
            cursor.execute(sql_update, (new_availability, item_id))
            db.commit()
            flash('Item availability updated successfully!', 'success')
        else:
            flash('Item availability not found.', 'error')

    except Exception as e:
        print(f"Error toggling item availability: {str(e)}")
        db.rollback()
        flash('Failed to toggle item availability. Please try again.', 'error')

    return redirect(url_for('item_management', shop_id=1))  # Replace 1 with actual shop_id

# Example route for order management
@app.route('/order_management/<int:shop_id>')
def order_management(shop_id):
    # Add your order management logic here
    return f"Order Management for Shop ID: {shop_id}"

# Example route for human resource management
@app.route('/human_resource_management/<int:shop_id>')
def human_resource_management(shop_id):
    # Add your human resource management logic here
    return f"Human Resource Management for Shop ID: {shop_id}"

# Example route for sales management
@app.route('/sales_management/<int:shop_id>')
def sales_management(shop_id):
    # Add your sales management logic here
    return f"Sales Management for Shop ID: {shop_id}"

# Example route for shop management
@app.route('/shop_management/<int:shop_id>')
def shop_management(shop_id):
    # Add your shop management logic here
    return f"Shop Management for Shop ID: {shop_id}"


@app.route('/kwetu_admin')
def kwetu_admin():
    with pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    ) as db:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM shops")
            shops = cursor.fetchall()
    show_register_link = True
    return render_template('kwetu_admin.html', shops=shops, show_register_link=show_register_link, os=os)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('signup'))

        try:
            with db.cursor() as cursor:
                sql = "INSERT INTO users (name, email, phone, password) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (name, email, phone, password))
                db.commit()
                flash('Signup successful! Please login.', 'success')
                return redirect(url_for('login'))
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'danger')
            return redirect(url_for('signup'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with db.cursor() as cursor:
            sql_user = "SELECT * FROM users WHERE email = %s AND password = %s"
            sql_shop = "SELECT * FROM shops WHERE email = %s AND password = %s"

            cursor.execute(sql_user, (email, password))
            user = cursor.fetchone()

            if user:
                session['user_id'] = user['id']
                session['user_name'] = user['name']
                session['role'] = 'user'
                flash('Login successful!', 'success')
                return redirect(url_for('index'))

            cursor.execute(sql_shop, (email, password))
            shop = cursor.fetchone()

            if shop:
                session['user_id'] = shop['id']
                session['user_name'] = shop['shop_name']
                session['role'] = 'shop'
                flash('Login successful!', 'success')
                return redirect(url_for('shop_dashboard', shop_id=shop['id']))

            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/register_shop', methods=['GET', 'POST'])
def register_shop():
    if request.method == 'POST':
        shop_name = request.form['shop_name']
        location = request.form['location']
        email = request.form['email']
        password = request.form['password']

        # Check if email already exists
        with db.cursor() as cursor:
            cursor.execute("SELECT email FROM shops WHERE email = %s", (email,))
            existing_email = cursor.fetchone()

        if existing_email:
            flash('Email already exists. Please use a different email.', 'error')
            return redirect(url_for('register_shop'))

        # Handle shop image upload
        if 'shop_image' in request.files:
            shop_image = request.files['shop_image']
            if shop_image.filename != '':
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], shop_image.filename)
                shop_image.save(image_path)
            else:
                image_path = None
        else:
            image_path = None

        # Insert shop data into MySQL
        with db.cursor() as cursor:
            cursor.execute("INSERT INTO shops (shop_name, location, shop_image, email, password) VALUES (%s, %s, %s, %s, %s)",
                           (shop_name, location, image_path, email, password))
            db.commit()

        flash('Shop registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register_shop.html')



if __name__ == '__main__':
    app.run(debug=True)