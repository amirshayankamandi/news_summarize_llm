import React from 'react';

const SummaryList = ({ summaries, preferences }) => {
    return (
        <div className="max-w-3xl mx-auto p-6 bg-base-200 rounded-lg shadow-md">

            {summaries.length ? (
                summaries.map((summary, index) => (
                    <div key={index} className="card mb-4 bg-base-100 shadow-lg">
                        {summary.image && (
                            <figure>
                                <img
                                    src={summary.image}
                                    alt={summary.title || "Article"}
                                    className="w-full h-48 object-cover rounded-t-lg"
                                />
                            </figure>
                        )}
                        <div className="card-body">
                            <h2 className="card-title">{summary.title}</h2>
                            <p>{summary.description}</p>
                            <div className="flex flex-wrap gap-2 mb-4">
                                {preferences && preferences.length > 0 && preferences.map((pref, index) => (
                                    <span
                                        key={index}
                                        className="px-3 py-1 text-xs font-medium text-white bg-blue-500 rounded-full"
                                    >
                                        {pref}
                                    </span>
                                ))}
                            </div>
                            {summary.url && (
                                <div className="card-actions justify-end">
                                    <a href={summary.url} className="btn btn-link text-blue-500">
                                        Read full article
                                    </a>
                                </div>
                            )}
                        </div>
                    </div>
                ))
            ) : (
                <div className="flex flex-col items-center justify-center py-6">
                    <svg className="w-12 h-12 text-gray-500 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12h6m-3-3v6m0-6a9 9 0 100 18 9 9 0 000-18z"></path>
                    </svg>
                    <p className="text-lg text-gray-600">Sorry, no news available.</p>
                </div>
            )}
        </div>
    );
};

export default SummaryList;
