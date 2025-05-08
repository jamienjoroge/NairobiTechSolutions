import { CommandLineIcon, ShieldCheckIcon, DevicePhoneMobileIcon, ServerIcon, ClipboardDocumentListIcon } from '@heroicons/react/24/outline';
import { ServiceCard } from '@/lib/types';

const services: ServiceCard[] = [
  {
    icon: <ShieldCheckIcon className="h-8 w-8 text-[#1E3A8A]" />,
    title: "ERP Implementation",
    description: "SAP, Odoo, Microsoft Dynamics tailored for SMEs."
  },
  {
    icon: <CommandLineIcon className="h-8 w-8 text-[#1E3A8A]" />,
    title: "Custom Software",
    description: "Bespoke solutions for logistics, healthcare, and finance."
  },
  {
    icon: <DevicePhoneMobileIcon className="h-8 w-8 text-[#1E3A8A]" />,
    title: "Web/Mobile Dev",
    description: "React, Flutter, Next.js apps with SEO optimization."
  },
  {
    icon: <ServerIcon className="h-8 w-8 text-[#1E3A8A]" />,
    title: "IT Support",
    description: "24/7 maintenance, cloud migration, cybersecurity."
  },
  {
    icon: <ClipboardDocumentListIcon className="h-8 w-8 text-[#1E3A8A]" />,
    title: "IT Project Management",
    description: "Agile methodologies, risk management, and stakeholder coordination."
  }
];

const ServicesSection = () => {
  return (
    <section id="services" className="py-20 bg-gray-50">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl font-bold text-[#1E3A8A] mb-4">Our Services</h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">Comprehensive technology solutions tailored for African businesses</p>
        </div>
        
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
          {services.map((service, index) => (
            <div key={index} className="bg-white rounded-lg shadow-md p-6 card-hover">
              <div className="h-14 w-14 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                {service.icon}
              </div>
              <h3 className="text-xl font-semibold mb-2 text-[#1E3A8A]">{service.title}</h3>
              <p className="text-gray-600 text-sm">{service.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default ServicesSection;
