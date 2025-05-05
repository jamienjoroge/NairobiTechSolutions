import { FaLinkedin, FaTwitter, FaGithub } from 'react-icons/fa';

const Footer = () => {
  return (
    <footer className="bg-[#1E3A8A] text-white py-12">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <div className="flex items-center mb-4">
              <div className="h-8 w-8 bg-[#F97316] rounded-md flex items-center justify-center">
                <span className="text-white font-bold">S</span>
              </div>
              <span className="ml-2 text-xl font-semibold">SaharaNova</span>
            </div>
            <p className="mb-4 text-gray-300">Transforming African businesses through innovative technology solutions.</p>
            <div className="flex space-x-4">
              <a href="#" className="text-gray-300 hover:text-[#F97316] transition-colors">
                <FaLinkedin className="h-5 w-5" />
              </a>
              <a href="#" className="text-gray-300 hover:text-[#F97316] transition-colors">
                <FaTwitter className="h-5 w-5" />
              </a>
              <a href="#" className="text-gray-300 hover:text-[#F97316] transition-colors">
                <FaGithub className="h-5 w-5" />
              </a>
            </div>
          </div>
          
          <div>
            <h3 className="text-lg font-semibold mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li><a href="#home" className="text-gray-300 hover:text-[#F97316] transition-colors">Home</a></li>
              <li><a href="#services" className="text-gray-300 hover:text-[#F97316] transition-colors">Services</a></li>
              <li><a href="#about" className="text-gray-300 hover:text-[#F97316] transition-colors">About Us</a></li>
              <li><a href="#contact" className="text-gray-300 hover:text-[#F97316] transition-colors">Contact</a></li>
            </ul>
          </div>
          
          <div>
            <h3 className="text-lg font-semibold mb-4">Newsletter</h3>
            <p className="mb-4 text-gray-300">Stay updated with our latest news and offers.</p>
            <form className="flex" onSubmit={(e) => e.preventDefault()}>
              <input 
                type="email" 
                placeholder="Your email" 
                className="px-4 py-2 bg-gray-800 text-white border border-gray-700 rounded-l-md focus:outline-none focus:ring-1 focus:ring-[#F97316]"
              />
              <button 
                type="submit" 
                className="bg-[#F97316] px-4 py-2 rounded-r-md hover:bg-orange-600 transition-colors"
              >
                Subscribe
              </button>
            </form>
          </div>
        </div>
        
        <div className="mt-12 pt-8 border-t border-gray-800 text-center text-gray-300">
          <p>© 2024 SaharaNova. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
