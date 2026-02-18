const VerdictBadge = ({ verdict }) => {
  let color = "gray";

  if (verdict === "Strong Fit") color = "green";
  if (verdict === "Moderate Fit") color = "orange";
  if (verdict === "Weak Fit") color = "red";

  return (
    <div className={`verdict ${color}`}>
      {verdict}
    </div>
  );
};

export default VerdictBadge;
