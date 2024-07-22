import React, { useState } from 'react';
import PreferencesForm from './components/PreferencesForm';
import SummaryList from './components/SummaryList';

const App = () => {
    const [summaries, setSummaries] = useState([]);
    const [loading, setLoading] = useState(false);
    const [preferences, setPreferences] = useState([]);

    const handlePreferencesSubmit = async (preferences) => {
        setLoading(true);
        setPreferences(preferences); // Update preferences state
        try {
            const response = await fetch('http://localhost:5001/summarize', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ preferences }),
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            setSummaries(data.summaries);
        } catch (error) {
            console.error('Error fetching summaries:', error);
            setSummaries([]);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-base-200 flex flex-col items-center py-6">
            <h1 className="text-4xl font-bold mb-6">News Summarizer</h1>
            <PreferencesForm onSubmit={handlePreferencesSubmit} />
            {loading ? (
                <div className="flex flex-col items-center justify-center py-6">
                    <div className="relative w-16 h-16">
                        <div className="absolute inset-0 flex items-center justify-center">
                            <div className="w-12 h-12 border-t-4 border-blue-500 border-solid rounded-full animate-spin"></div>
                        </div>
                    </div>
                    <p className="text-lg text-gray-600 mt-4">Fetching your news...</p>
                </div>
            ) : (
                <SummaryList summaries={summaries} preferences={preferences} />
            )}
        </div>
    );
};

export default App;
