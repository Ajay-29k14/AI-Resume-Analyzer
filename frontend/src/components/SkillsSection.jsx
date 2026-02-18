const SkillsSection = ({ matched, missing }) => {
  return (
    <div className="skills-container">
      <div>
        <h3>Matched Skills</h3>
        <ul>
          {matched.map((skill, index) => (
            <li key={index} className="matched">
              {skill}
            </li>
          ))}
        </ul>
      </div>

      <div>
        <h3>Missing Skills</h3>
        <ul>
          {missing.map((skill, index) => (
            <li key={index} className="missing">
              {skill}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default SkillsSection;
