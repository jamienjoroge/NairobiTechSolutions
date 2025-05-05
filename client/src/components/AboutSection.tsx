import { CheckCircleIcon } from '@heroicons/react/24/outline';

const values = [
  "Local talent, global standards",
  "Innovative problem solving",
  "Sustainable tech practices",
  "Client-centered approach"
];

const AboutSection = () => {
  return (
    <section id="about" className="py-20 gradient-bg text-white">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl font-bold mb-4">About SaharaNova</h2>
          <p className="text-xl max-w-3xl mx-auto">Founded in Nairobi, serving Africa's tech needs since 2024.</p>
        </div>
        
        <div className="max-w-4xl mx-auto">
          <div className="bg-white/10 backdrop-blur-sm p-8 rounded-lg shadow-lg">
            <div className="flex flex-col md:flex-row items-center gap-8">
              <div className="md:w-1/3">
                <img 
                  src="https://images.unsplash.com/photo-1572204292164-b35ba943fca7?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" 
                  alt="Nairobi skyline" 
                  className="rounded-lg shadow-lg w-full h-auto aspect-square object-cover"
                  loading="lazy"
                />
              </div>
              <div className="md:w-2/3">
                <h3 className="text-2xl font-semibold mb-4">Our Mission</h3>
                <p className="mb-6 text-lg">Bridging gaps with scalable, future-proof software solutions that empower African businesses to compete globally.</p>
                
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  {values.map((value, index) => (
                    <div key={index} className="flex items-center gap-2">
                      <CheckCircleIcon className="h-5 w-5 text-[#F97316]" />
                      <span>{value}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;
