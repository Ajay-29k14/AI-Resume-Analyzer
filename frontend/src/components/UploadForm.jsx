import { useState } from "react";
import { analyzeResume } from "../services/api";

const UploadForm = ({ setResult }) => {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!resume || !jobDescription) {
      alert("Please upload resume and enter job description");
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
      console.error(error);
      alert("Error analyzing resume");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form">
      <input
        type="file"
        accept=".pdf,.docx"
        onChange={(e) => setResume(e.target.files[0])}
      />

      <textarea
        placeholder="Paste job description here..."
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
      />

      <button type="submit">
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>
    </form>
  );
};

export default UploadForm;
