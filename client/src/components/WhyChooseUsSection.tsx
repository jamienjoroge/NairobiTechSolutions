import { CheckIcon } from '@heroicons/react/24/solid';

const reasons = [
  {
    title: "African Expertise",
    description: "Built in Kenya, we understand the unique challenges and opportunities of African businesses."
  },
  {
    title: "Tailored Solutions",
    description: "We don't believe in one-size-fits-all. Every solution is customized to your specific needs."
  },
  {
    title: "Future-Proof Technology",
    description: "We implement scalable solutions that grow with your business and adapt to changing markets."
  }
];

const WhyChooseUsSection = () => {
  return (
    <section className="py-20 bg-white">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col lg:flex-row items-center gap-12">
          <div className="lg:w-1/2">
            <img 
              src="https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" 
              alt="Tech consultancy team meeting" 
              className="rounded-lg shadow-xl w-full h-auto object-cover"
              loading="lazy"
            />
          </div>
          <div className="lg:w-1/2">
            <h2 className="text-3xl font-bold text-[#1E3A8A] mb-6">Why Partner With Us?</h2>
            
            <div className="space-y-6">
              {reasons.map((reason, index) => (
                <div key={index} className="flex gap-4">
                  <div className="flex-shrink-0 h-10 w-10 bg-[#F97316] rounded-full flex items-center justify-center text-white">
                    <CheckIcon className="h-5 w-5" />
                  </div>
                  <div>
                    <h3 className="text-xl font-semibold mb-1">{reason.title}</h3>
                    <p className="text-gray-600">{reason.description}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default WhyChooseUsSection;
