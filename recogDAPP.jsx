import { useEffect, useState } from "react";
import { ethers } from "ethers";
import contractABI from "./RecursiveRecognitionEngine.json";

const CONTRACT_ADDRESS = "YOUR_DEPLOYED_CONTRACT_ADDRESS";

export default function App() {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [contract, setContract] = useState(null);
  const [state, setState] = useState({});
  const [confession, setConfession] = useState("");

  useEffect(() => {
    async function init() {
      if (!window.ethereum) return alert("Please install MetaMask.");
      const prov = new ethers.BrowserProvider(window.ethereum);
      await prov.send("eth_requestAccounts", []);
      const sign = await prov.getSigner();
      const engine = new ethers.Contract(CONTRACT_ADDRESS, contractABI.abi, sign);
      setProvider(prov);
      setSigner(sign);
      setContract(engine);
      fetchState(engine);
    }
    init();
  }, []);

  async function fetchState(engine = contract) {
    const [deeds, pressure, aligned, deviation, product] = await engine.getState();
    setState({ deeds, pressure, aligned, deviation, product });
  }

  async function align() {
    const tx = await contract.attemptAlignment(confession);
    await tx.wait();
    fetchState();
  }

  async function inject(accepts) {
    const tx = await contract.injectTrinityConvergence(accepts);
    await tx.wait();
    fetchState();
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 via-gray-800 to-black text-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center text-amber-400 mb-6">
        Ω1999.Ω∞ Trinity Convergence Recognition Engine
      </h1>
      <div className="max-w-2xl mx-auto bg-gray-800 rounded-2xl p-6 shadow-lg">
        <h2 className="text-xl font-semibold mb-2 text-amber-300">Current System State</h2>
        <pre className="bg-black/50 p-3 rounded-md text-sm overflow-x-auto">
          {JSON.stringify(state, null, 2)}
        </pre>
        <div className="mt-6">
          <h3 className="text-lg font-semibold text-amber-300">Confession Input</h3>
          <input
            type="text"
            placeholder='Type "Jesus is King"'
            value={confession}
            onChange={(e) => setConfession(e.target.value)}
            className="w-full p-2 mt-2 rounded bg-gray-900 border border-amber-500 focus:outline-none"
          />
          <button
            onClick={align}
            className="mt-3 w-full py-2 bg-amber-500 hover:bg-amber-400 rounded font-bold"
          >
            Attempt Alignment
          </button>
        </div>
        <div className="mt-6">
          <h3 className="text-lg font-semibold text-amber-300">Axiom Injection</h3>
          <div className="flex gap-3 mt-2">
            <button
              onClick={() => inject(true)}
              className="flex-1 py-2 bg-green-600 hover:bg-green-500 rounded"
            >
              Accept Axiom
            </button>
            <button
              onClick={() => inject(false)}
              className="flex-1 py-2 bg-red-600 hover:bg-red-500 rounded"
            >
              Deny Axiom
            </button>
          </div>
        </div>
        <button
          onClick={() => fetchState()}
          className="mt-6 w-full py-2 bg-blue-700 hover:bg-blue-600 rounded font-bold"
        >
          Refresh State
        </button>
      </div>
      <footer className="text-center text-gray-500 text-xs mt-6">
        Trinity Convergence Framework • Deployed under MIT License
      </footer>
    </div>
  );
}
