export function Footer() {
	return (
		<footer className="grid gap-10 sm:flex justify-around sm:pl-[100px] py-[100px] bg-brand-yellow/10">
			<div className="grid gap-2">
				<a href="/">
					<img src="/nyumbani-logo.svg" className="w-[200px]" alt="nyumbani logo" />
				</a>
				<div>
					<p>+254757884803</p>
					<p>shop@nyumbanigreens.com</p>
					<p className="text-neutral-400 font-bold">Nairobi, Kenya</p>
					<p className="flex gap-2 items-center">
						<span>
							{' '}
							<img width={16} src="/images/whatsapp-logo.webp" alt="whatsapp logo" />
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
					<input className="border hover:border-brand-green p-2" placeholder="First Name" />
					<input className="border hover:border-brand-green p-2" type="email" placeholder="Email" />
					<div>
						<button type="submit" className="bg-black text-white text-sm py-[10px] px-[24px]">
							Submit
						</button>
					</div>
				</form>
				<div className="flex items-center gap-4 pt-4 text-black">
					<a
						target="_blank"
						rel="noreferrer"
						className="text-muted-foreground hover:text-foreground p-2 rounded-md"
						href="https://web.facebook.com/profile.php?id=61557078042281"
					>
						<svg
							className="h-5 w-5"
							xmlns="http://www.w3.org/2000/svg"
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
						>
							<title>Facebook</title>
							<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z" />
						</svg>
						<span className="sr-only">Facebook</span>
					</a>
					<a
						target="_blank"
						rel="noreferrer"
						className="text-muted-foreground hover:text-foreground  p-2 rounded-md"
						href="https://x.com/NyumbaniGreens"
					>
						<svg
							className="h-5 w-5"
							xmlns="http://www.w3.org/2000/svg"
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
						>
							<title>Twitter</title>
							<path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z" />
						</svg>
						<span className="sr-only">Twitter</span>
					</a>
					<a
						target="_blank"
						rel="noreferrer"
						className="text-muted-foreground hover:text-foreground p-2 rounded-md"
						href="https://www.instagram.com/nyumbanigreens/?hl=en"
					>
						<svg
							className="h-5 w-5"
							xmlns="http://www.w3.org/2000/svg"
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
						>
							<title>Instagram</title>
							<rect width="20" height="20" x="2" y="2" rx="5" ry="5" />
							<path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" />
							<line x1="17.5" x2="17.51" y1="6.5" y2="6.5" />
						</svg>
						<span className="sr-only">Instagram</span>
					</a>
					<a
						target="_blank"
						className="text-muted-foreground hover:text-foreground  p-2 rounded-md"
						href="https://www.linkedin.com/company/nyumbani-greens/"
						rel="noreferrer"
					>
						<svg
							className="h-5 w-5"
							xmlns="http://www.w3.org/2000/svg"
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
						>
							<title>LinkedIn</title>
							<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z" />
							<rect width="4" height="12" x="2" y="9" />
							<circle cx="4" cy="4" r="2" />
						</svg>
						<span className="sr-only">LinkedIn</span>
					</a>
				</div>
			</div>
		</footer>
	);
}
