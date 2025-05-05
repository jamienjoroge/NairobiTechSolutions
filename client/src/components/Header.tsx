import { useState, useEffect } from 'react';
import { Link } from 'wouter';

const Header = () => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);
  
  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);
  
  const toggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };
  
  const closeMobileMenu = () => {
    setMobileMenuOpen(false);
  };
  
  return (
    <header className={`fixed w-full bg-white/90 backdrop-blur-sm z-50 ${isScrolled ? 'shadow-md' : 'shadow-sm'}`}>
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex-shrink-0 flex items-center">
            <div className="flex items-center">
              <div className="h-8 w-8 bg-[#F97316] rounded-md flex items-center justify-center">
                <span className="text-white font-bold">S</span>
              </div>
              <span className="ml-2 text-xl font-semibold text-[#1E3A8A]">SaharaNova</span>
            </div>
          </div>
          
          {/* Desktop Navigation */}
          <div className="hidden md:flex md:items-center md:space-x-8">
            <a href="#home" className="text-gray-700 hover:text-[#1E3A8A] font-medium transition-colors">Home</a>
            <a href="#services" className="text-gray-700 hover:text-[#1E3A8A] font-medium transition-colors">Services</a>
            <a href="#about" className="text-gray-700 hover:text-[#1E3A8A] font-medium transition-colors">About</a>
            <a href="#contact" className="orange-gradient text-white px-4 py-2 rounded-md font-medium hover:shadow-lg transition-shadow">Contact Us</a>
          </div>
          
          {/* Mobile Menu Button */}
          <div className="flex items-center md:hidden">
            <button 
              type="button" 
              onClick={toggleMobileMenu}
              className="text-gray-700 hover:text-[#1E3A8A]"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
        </div>
        
        {/* Mobile Navigation Menu */}
        <div className={`md:hidden ${mobileMenuOpen ? 'block' : 'hidden'}`}>
          <div className="px-2 pt-2 pb-3 space-y-1">
            <a href="#home" onClick={closeMobileMenu} className="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-[#1E3A8A] hover:bg-gray-50">Home</a>
            <a href="#services" onClick={closeMobileMenu} className="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-[#1E3A8A] hover:bg-gray-50">Services</a>
            <a href="#about" onClick={closeMobileMenu} className="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-[#1E3A8A] hover:bg-gray-50">About</a>
            <a href="#contact" onClick={closeMobileMenu} className="block px-3 py-2 rounded-md text-base font-medium orange-gradient text-white">Contact Us</a>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header;
