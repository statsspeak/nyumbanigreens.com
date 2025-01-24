import React from 'react';
import { cn } from '../../utils/cn';
import { ShoppingBagIcon } from 'lucide-react';

type ButtonProps = React.DetailedHTMLProps<React.AnchorHTMLAttributes<HTMLAnchorElement>, HTMLAnchorElement>;
function ButtonShoptoday(props: ButtonProps) {
	const { className, ...rest } = props;
	return (
		<a
			{...rest}
			href="/catalogue"
			className={cn('flex gap-4 items-center bg-black text-white text-sm py-[10px] px-[24px]', className)}
		>
			<ShoppingBagIcon />
			Shop Today
		</a>
	);
}

export default function Home() {
	const styles = {
		howItWorks: {
			h3: 'text-2xl font-bold text-green-800',
		},
	};

	return (
		<section className="grid grid-cols-[1fr_1fr]">
			<div className="main-left">
				<div className="flex">
					<nav className="px-[32px] py-[12px] flex gap-[50px] ml-auto cursor-pointer [&>a]:hover:underline">
						<a href="/contacts">Contact</a>
						<a href="/catalogue">Shop</a>
					</nav>
				</div>
				<div className="hero grid items-center justify-center h-svh  px-[32px]">
					<p className="grid gap-4 text-7xl font-[arialrounded]">
						<span className="mb-4">
							Local, Organic, <br />
							African Vegetables <br />
							Delivered to Your Door!
						</span>

						<span>
							<ButtonShoptoday className="inline-flex" />
						</span>
					</p>

					<div className="flex flex-col gap-8">
						<div className="flex">
							<h2 className="text-2xl text-yellow-600">How it works</h2>
						</div>
						<br />
						<div>
							<h3 className={styles.howItWorks.h3}>Order</h3>
							Choose the option that works best. No matter what we'll do our best to fulfill.
						</div>
						<div>
							<h3 className={styles.howItWorks.h3}>Delivery</h3>
							The nyumbani team packs every box with utmost care and controls. We'll do everything it
							takes to get it to your door.
						</div>
						<div>
							<h3 className={styles.howItWorks.h3}>Enjoy</h3>
							Healthy produce, minimal packaging, and jobs created. Let's eat!
						</div>
					</div>

					<ButtonShoptoday className="ml-auto" />
				</div>
			</div>
			<div className="flex justify-end">
				<img className="h-svh" src="/images/markus-spiske--unsplash.jpg" />
			</div>
		</section>
	);
}
