import { TeamMember } from '@/lib/types';

const teamMembers: TeamMember[] = [
  {
    name: "Sarah Kimani",
    position: "Chief Technology Officer",
    bio: "10+ years experience in enterprise software architecture and ERP implementation.",
    image: "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80"
  },
  {
    name: "David Ochieng",
    position: "Solutions Architect",
    bio: "Specialized in designing scalable systems for African market challenges.",
    image: "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80"
  },
  {
    name: "Grace Mwangi",
    position: "Development Lead",
    bio: "Full-stack developer with expertise in React, Flutter, and cloud technologies.",
    image: "https://images.unsplash.com/photo-1580894732444-8ecded7900cd?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80"
  }
];

const TeamSection = () => {
  return (
    <section className="py-20 bg-gray-50">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl font-bold text-[#1E3A8A] mb-4">Our Team</h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">Meet the experts who bring your digital vision to life</p>
        </div>
        
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {teamMembers.map((member, index) => (
            <div key={index} className="bg-white rounded-lg shadow-md overflow-hidden card-hover">
              <img 
                src={member.image} 
                alt={`Team member - ${member.position}`} 
                className="w-full h-64 object-cover"
                loading="lazy"
              />
              <div className="p-6">
                <h3 className="text-xl font-semibold text-[#1E3A8A]">{member.name}</h3>
                <p className="text-[#F97316] font-medium mb-3">{member.position}</p>
                <p className="text-gray-600">{member.bio}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default TeamSection;
