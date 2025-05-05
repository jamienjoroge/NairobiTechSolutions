import { MapPinIcon, PhoneIcon, EnvelopeIcon } from '@heroicons/react/24/outline';
import { FaLinkedin, FaTwitter, FaGithub } from 'react-icons/fa';
import ContactForm from './ContactForm';
import { ContactInfo } from '@/lib/types';

const contactDetails: ContactInfo[] = [
  {
    icon: <MapPinIcon className="h-5 w-5 text-[#1E3A8A]" />,
    title: "Address",
    value: "Waiyaki Way, Nairobi, Kenya",
    link: "#"
  },
  {
    icon: <PhoneIcon className="h-5 w-5 text-[#1E3A8A]" />,
    title: "Phone",
    value: "+254 794 122747",
    link: "tel:+254794122747"
  },
  {
    icon: <EnvelopeIcon className="h-5 w-5 text-[#1E3A8A]" />,
    title: "Email",
    value: "hello@saharanova.com",
    link: "mailto:hello@saharanova.com"
  }
];

const ContactSection = () => {
  return (
    <section id="contact" className="py-20 bg-white">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl font-bold text-[#1E3A8A] mb-4">Get In Touch</h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">Ready to transform your business? Contact us for a free consultation.</p>
        </div>
        
        <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12">
          <div>
            <div className="bg-gray-50 rounded-lg p-8 shadow-md">
              <h3 className="text-2xl font-semibold text-[#1E3A8A] mb-6">Contact Information</h3>
              
              <div className="space-y-6">
                {contactDetails.map((detail, index) => (
                  <div key={index} className="flex items-start gap-4">
                    <div className="flex-shrink-0 h-10 w-10 bg-blue-100 rounded-lg flex items-center justify-center">
                      {detail.icon}
                    </div>
                    <div>
                      <h4 className="text-lg font-medium mb-1">{detail.title}</h4>
                      {detail.link ? (
                        <a href={detail.link} className="text-[#1E3A8A] hover:text-[#F97316] transition-colors">
                          {detail.value}
                        </a>
                      ) : (
                        <p className="text-gray-600">{detail.value}</p>
                      )}
                    </div>
                  </div>
                ))}
              </div>
              
              <div className="mt-8">
                <h4 className="text-lg font-medium mb-4">Connect With Us</h4>
                <div className="flex space-x-4">
                  <a href="#" className="h-10 w-10 bg-[#1E3A8A] rounded-full flex items-center justify-center text-white hover:bg-[#F97316] transition-colors">
                    <FaLinkedin className="h-5 w-5" />
                  </a>
                  <a href="#" className="h-10 w-10 bg-[#1E3A8A] rounded-full flex items-center justify-center text-white hover:bg-[#F97316] transition-colors">
                    <FaTwitter className="h-5 w-5" />
                  </a>
                  <a href="#" className="h-10 w-10 bg-[#1E3A8A] rounded-full flex items-center justify-center text-white hover:bg-[#F97316] transition-colors">
                    <FaGithub className="h-5 w-5" />
                  </a>
                </div>
              </div>
            </div>
            
            <div className="mt-8 h-[300px] bg-gray-200 rounded-lg shadow-md overflow-hidden">
              <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.818394419901!2d36.76098867365523!3d-1.2636369356242788!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x182f173c0a1d6c7d%3A0x2f88240f40150fdb!2sWaiyaki%20Way%2C%20Nairobi!5e0!3m2!1sen!2ske!4v1696858920423!5m2!1sen!2ske" 
                width="100%" 
                height="100%" 
                style={{ border: 0 }}
                allowFullScreen 
                loading="lazy" 
                referrerPolicy="no-referrer-when-downgrade"
                title="SaharaNova Office Location"
              ></iframe>
            </div>
          </div>
          
          <ContactForm />
        </div>
      </div>
    </section>
  );
};

export default ContactSection;
