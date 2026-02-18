import { useState } from "react";
import { analyzeResume } from "./services/api";

function App() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async (e) => {
    e.preventDefault();

    if (!resume || !jobDescription) {
      alert("Upload resume and enter job description");
      return;
    }

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {
      setLoading(true);
      const data = await analyzeResume(formData);
      setResult(data);
    } catch (error) {
      alert("Backend not running or error occurred");
    } finally {
      setLoading(false);
    }
  };

  const getVerdictColor = (verdict) => {
    if (verdict === "Strong Fit") return "#16a34a";
    if (verdict === "Moderate Fit") return "#f59e0b";
    return "#dc2626";
  };

  return (
    <div style={pageStyle}>
      <div style={cardStyle}>
        <h1 style={{ marginBottom: "20px" }}>AI Resume Analyzer</h1>

        <form onSubmit={handleAnalyze} style={formStyle}>
          <input
            type="file"
            accept=".pdf,.docx"
            onChange={(e) => setResume(e.target.files[0])}
          />

          <textarea
            placeholder="Paste Job Description Here..."
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            rows={6}
          />

          <button style={buttonStyle} type="submit">
            {loading ? "Analyzing..." : "Analyze Resume"}
          </button>
        </form>

        {result && (
          <div style={{ marginTop: "30px" }}>
            <div style={scoreContainer}>
              <div style={scoreBox}>
                <h3>Match %</h3>
                <p style={bigNumber}>{result.match_percentage}%</p>
              </div>

              <div style={scoreBox}>
                <h3>ATS Score</h3>
                <p style={bigNumber}>{result.ats_score}%</p>
              </div>
            </div>

            <div style={skillsContainer}>
              <div>
                <h3>Matched Skills</h3>
                {result.matched_skills.map((skill, i) => (
                  <span key={i} style={matchedSkill}>
                    {skill}
                  </span>
                ))}
              </div>

              <div>
                <h3>Missing Skills</h3>
                {result.missing_skills.map((skill, i) => (
                  <span key={i} style={missingSkill}>
                    {skill}
                  </span>
                ))}
              </div>
            </div>

            <div
              style={{
                marginTop: "25px",
                padding: "15px",
                textAlign: "center",
                borderRadius: "8px",
                backgroundColor: getVerdictColor(result.verdict),
                color: "white",
                fontWeight: "bold",
                fontSize: "18px",
              }}
            >
              {result.verdict}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

/* ---------------- Styles ---------------- */

const pageStyle = {
  minHeight: "100vh",
  backgroundColor: "#f3f4f6",
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  padding: "20px",
};

const cardStyle = {
  width: "900px",
  backgroundColor: "white",
  padding: "40px",
  borderRadius: "12px",
  boxShadow: "0 10px 30px rgba(0,0,0,0.1)",
};

const formStyle = {
  display: "flex",
  flexDirection: "column",
  gap: "15px",
};

const buttonStyle = {
  padding: "12px",
  backgroundColor: "#2563eb",
  color: "white",
  border: "none",
  borderRadius: "6px",
  fontWeight: "bold",
  cursor: "pointer",
};

const scoreContainer = {
  display: "flex",
  justifyContent: "space-between",
  marginTop: "20px",
};

const scoreBox = {
  width: "45%",
  backgroundColor: "#f9fafb",
  padding: "20px",
  borderRadius: "10px",
  textAlign: "center",
};

const bigNumber = {
  fontSize: "32px",
  fontWeight: "bold",
};

const skillsContainer = {
  display: "flex",
  justifyContent: "space-between",
  marginTop: "20px",
};

const matchedSkill = {
  display: "inline-block",
  backgroundColor: "#dcfce7",
  color: "#166534",
  padding: "6px 10px",
  borderRadius: "20px",
  margin: "5px",
};

const missingSkill = {
  display: "inline-block",
  backgroundColor: "#fee2e2",
  color: "#7f1d1d",
  padding: "6px 10px",
  borderRadius: "20px",
  margin: "5px",
};

export default App;
