import type React from 'react';
import { cn } from '../../utils/cn';
import { ShoppingBagIcon } from 'lucide-react';
import { Footer } from '../components/compositions/footer';

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
	return (
		<>
			{' '}
			<section className="flex">
				<div className="main-left flex-1">
					<div className="flex">
						<nav className="px-[32px] py-[12px] flex gap-2 ml-auto cursor-pointer [&>a]:hover:underline">
							{[
								{ href: '/contacts', text: 'Contact' },
								{
									href: '/theteam',
									text: 'Meet the team',
								},
								{ href: '/shop', text: 'Shop' },
							].map((item, index) => (
								<>
									<a key={item.text} href={item.href}>
										{item.text}
									</a>
									{index < 2 && '•'}
								</>
							))}
						</nav>
					</div>
					<div className="hero grid items-center justify-center min-h-svh  px-[32px]">
						<p className="grid gap-4 text-7xl font-[arialrounded]">
							<span className="mb-4">
								Local, Organic, <br />
								Indigenous Vegetables <br />
								Delivered to Your Door!
							</span>

							<span>
								<ButtonShoptoday className="inline-flex" />
							</span>
						</p>

						<div className="flex flex-col">
							<div className="flex mt-4">
								<h2 className="text-xl text-yellow-600">How it works</h2>
							</div>
							<br />
							<div className="hiw grid sm:flex gap-4">
								{[
									{
										title: 'Order',
										description:
											"Choose the option that works best. No matter what we'll do our best to fulfill.",
									},
									{
										title: 'Delivery',
										description:
											"The nyumbani team packs every box with utmost care and controls. We'll do everything it takes to get it to your door.",
									},
									{
										title: 'Enjoy',
										description: "Healthy produce, minimal packaging, and jobs created. Let's eat!",
									},
								].map((item) => (
									<div key={item.title} className="flex flex-col gap-4">
										<div className="flex items-center gap-6">
											<div className="inline-block w-[56px] h-[56px] rounded-[100px] overflow-hidden">
												<img className="h-[56px] " src="/images/vegetables.svg" alt="" />
											</div>
											<h3 className={'text-2xl font-bold text-green-800'}>{item.title}</h3>
										</div>
										<p>{item.description}</p>
									</div>
								))}
							</div>
						</div>

						<ButtonShoptoday className="ml-auto" />
					</div>
				</div>
				<div className="hidden sm:flex justify-end">
					<img className="h-svh" src="/images/markus-spiske--unsplash.jpg" alt="markus spiske unsplash" />
				</div>
			</section>
			<Footer />
		</>
	);
}
