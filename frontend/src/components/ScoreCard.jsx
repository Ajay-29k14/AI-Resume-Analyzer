const ScoreCard = ({ match, ats }) => {
  return (
    <div className="score-container">
      <div className="score-box">
        <h2>Match Percentage</h2>
        <p className="big-score">{match}%</p>
      </div>

      <div className="score-box">
        <h2>ATS Score</h2>
        <p className="big-score">{ats}%</p>
      </div>
    </div>
  );
};

export default ScoreCard;
