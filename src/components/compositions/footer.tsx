export function Footer() {
    return (
        <footer className="grid gap-10 sm:flex justify-around sm:pl-[100px] py-[100px] bg-brand-yellow/10">
            <div className="grid gap-2">
                <a href="/">
                    <img src="/nyumbani-logo.svg" className="w-[200px]" />
                </a>
                <div>
                    <p>+254757884803</p>
                    <p>shop@nyumbanigreens.com</p>
                    <p className="text-neutral-400 font-bold">Nairobi, Kenya</p>
                    <p className="flex gap-2 items-center">
                        <span>
                            {" "}
                            <img width={16} src="/images/whatsapp-logo.webp" />
                        </span>
                        <a href="https://wa.me/+254757884803">
                            Talk to us on <span className="underline text-green-700">Whatsapp</span>
                        </a>
                    </p>
                </div>
            </div>
            <div className="grid">
                <h2 className="uppercase font-black text-gray-500 text-xl">SUPPORT</h2>
                <div className="grid text-green-700">
                    <a href="/contacts">Contact</a>
                    <a href="/privacy">Privacy Policy</a>
                    <a href="/terms">Terms and Conditions</a>
                </div>
            </div>
            <div>
                <p>SIGN UP FOR NEWS AND DEALS!</p>
                <p className="max-w-[300px]">
                    A weekly newsletter, with product releases, recipes, and exclusive deals.
                </p>
                <form className="grid gap-2 pt-[32px]">
                    <input
                        className="border hover:border-brand-green p-2"
                        placeholder="First Name"
                    />
                    <input
                        className="border hover:border-brand-green p-2"
                        type="email"
                        placeholder="Email"
                    />
                    <div>
                        <button
                            type="submit"
                            className="bg-black text-white text-sm py-[10px] px-[24px]"
                        >
                            Submit
                        </button>
                    </div>
                </form>
            </div>
        </footer>
    );
}
