DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;

CREATE TABLE HealthAnalytics (
    analytics_id INT PRIMARY KEY,
    profile_id INT NOT NULL,
    average_weight DECIMAL(5,2),
    weight_trend TEXT,
    recommended_diet TEXT
);

INSERT INTO HealthAnalytics VALUES
(1, 1, 22.4, 'Stable', 'Continue current diet with added fiber');
