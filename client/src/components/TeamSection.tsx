import { TeamMember } from '@/lib/types';

const teamMembers: TeamMember[] = [
  {
    name: "James",
    position: "Chief Technology Officer",
    bio: "Leading our technical vision and innovation strategy with 15+ years of experience in enterprise architecture and digital transformation.",
    image: "/illustrations/cto.svg"
  },
  {
    name: "Grace",
    position: "Business Development Manager",
    bio: "Driving growth and partnerships across Africa with expertise in market expansion and strategic business development.",
    image: "/illustrations/business-manager.svg"
  },
  {
    name: "John",
    position: "Support Manager",
    bio: "Ensuring exceptional client support and service delivery with a focus on building long-term relationships and customer success.",
    image: "/illustrations/support-manager.svg"
  }
];

const TeamSection = () => {
  return (
    <section className="py-20 bg-gray-50">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl font-bold text-[#1E3A8A] mb-4">Our Leadership Team</h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">Meet the experts driving innovation and growth across Africa</p>
        </div>
        
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {teamMembers.map((member, index) => (
            <div key={index} className="bg-white rounded-lg shadow-md overflow-hidden card-hover transform transition-transform hover:scale-105">
              <div className="h-64 bg-gray-100 flex items-center justify-center p-4">
                <img 
                  src={member.image} 
                  alt={`${member.name} - ${member.position}`} 
                  className="w-full h-full object-contain"
                  loading="lazy"
                />
              </div>
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
