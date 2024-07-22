import React, { useState } from 'react';

const PreferencesForm = ({ onSubmit }) => {
    const [preferences, setPreferences] = useState([]);

    const handleCheckboxChange = (e) => {
        const { value, checked } = e.target;
        setPreferences(prev => {
            const updated = new Set(prev);
            if (checked) {
                updated.add(value);
            } else {
                updated.delete(value);
            }
            return Array.from(updated);
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (onSubmit) onSubmit(preferences);
    };

    return (
        <div className="max-w-xl mx-auto p-6 bg-base-200 rounded-lg shadow-md">
            <h2 className="text-lg font-semibold mb-4">Select Your Preferences</h2>
            <form onSubmit={handleSubmit} className="space-y-4">
                {["Technology", "Sports", "Business", "Health"].map(pref => (
                    <div key={pref} className="flex items-center">
                        <input
                            type="checkbox"
                            id={pref}
                            value={pref}
                            onChange={handleCheckboxChange}
                            className="checkbox"
                        />
                        <label htmlFor={pref} className="ml-2">{pref}</label>
                    </div>
                ))}
                <button
                    type="submit"
                    className="btn btn-primary w-full"
                >
                    Get Summaries
                </button>
            </form>
        </div>
    );
};

export default PreferencesForm;
