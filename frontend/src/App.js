import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import GUI from './gui';
function App() {  
  return (
    <Router>
      <Routes>
      <Route path="/" element={<GUI />} />
      </Routes>
    </Router>
  );
}

export default App;
