import type { Metadata } from 'next';
import '@fontsource-variable/plus-jakarta-sans';
import './globals.css';
export const metadata:Metadata={title:'Kenya Economic Observatory',description:'Explore Kenya’s economy through Central Bank data, economic research and source evidence.'};
export default function Layout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}
