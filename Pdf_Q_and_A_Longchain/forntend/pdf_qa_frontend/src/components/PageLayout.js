import React from 'react';
import PdfUploadZone from './PdfUploadZone';
import AskQuestionZone from './AskQuestionZone';
import History from './History';

const PageLayout = () => {
  return (
    <div className="layout">
      <div className="left-section">
        <History />
      </div>
      <div className="right-section">
        <div className="top-right-section">
          <PdfUploadZone />
        </div>
        <div className="bottom-right-section">
          <AskQuestionZone />
        </div>
      </div>
    </div>
  );
};

export default PageLayout;
