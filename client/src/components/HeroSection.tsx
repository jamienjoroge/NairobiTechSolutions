const HeroSection = () => {
  return (
    <section id="home" className="tech-wave-bg min-h-screen flex items-center relative pt-16">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-16 relative z-10">
        <div className="max-w-3xl mx-auto text-center text-white">
          <h1 className="text-3xl md:text-5xl font-bold mb-4">SaharaNova – Digital Transformation for Africa's Businesses</h1>
          <p className="text-xl mb-8 font-mono">ERP Solutions | Custom Software | Web & Mobile Development</p>
          <a href="#contact" className="bg-white text-[#1E3A8A] hover:bg-gray-100 px-8 py-3 rounded-full text-lg font-semibold inline-block transition-colors shadow-lg hover:shadow-xl">
            Get a Free Consultation
          </a>
        </div>
      </div>
      <div className="absolute bottom-0 left-0 right-0 h-20 bg-gradient-to-t from-gray-50 to-transparent"></div>
    </section>
  );
};

export default HeroSection;
