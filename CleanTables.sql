UPDATE skfrontendjobs
SET JobTypes = REPLACE(JobTypes, "[]", "NA"),
    JobTypes = REPLACE(JobTypes, "[", ""),
    JobTypes = REPLACE(JobTypes, "]", ""),
    JobTypes = REPLACE(JobTypes, "'", "");

UPDATE skfrontendjobs
SET Skills = REPLACE(Skills, "[]", "NA"),
    Skills = REPLACE(Skills, "[", ""),
    Skills = REPLACE(Skills, "]", ""),
    Skills = REPLACE(Skills, "'", "");

UPDATE skfrontendjobs
SET Education = REPLACE(Education, "[]", "NA"),
    Education = REPLACE(Education, "[", ""),
    Education = REPLACE(Education, "]", ""),
    Education = REPLACE(Education, "'", ""),
    Education = REPLACE(Education, '"', "");

SELECT COUNT(*) AS in_person_jobs FROM skfrontendjobs
WHERE WorkLocation = "In-person";

SELECT COUNT(*) AS hybrid_remote_jobs FROM skfrontendjobs
WHERE WorkLocation = "Hybrid remote";

SELECT COUNT(*) AS remote_jobs FROM skfrontendjobs
WHERE WorkLocation = "Remote";





SELECT COUNT(*) AS full_time FROM skfrontendjobs
WHERE JobTypes LIKE "%Full-time%";

SELECT COUNT(*) AS part_time FROM skfrontendjobs
WHERE JobTypes LIKE "%Part-time%";

SELECT COUNT(*) AS contract_time FROM skfrontendjobs
WHERE JobTypes LIKE "%Contract%";

SELECT COUNT(*) AS internship_time FROM skfrontendjobs
WHERE JobTypes LIKE "%Internship/Co-op%";





SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%sql%";

SELECT COUNT(*) FROM abfrontendjobs
WHERE Skills LIKE "%react%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%javascript%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%css%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%html%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%next.js%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%angular%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%aws%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%api%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%figma%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%jquery%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%git%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%restful%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%json%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%xml%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%node%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%c#%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%c++%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "% java %";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%python%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%cloud%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%linux%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%boostrap%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%django%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%express.js%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%rails%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%php%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Skills LIKE "%sass%";




SELECT COUNT(*) FROM skfrontendjobs
WHERE Education LIKE "%bachelors%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Education LIKE "%phd%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Education LIKE "%graduate%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Education LIKE "%masters%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Education LIKE "%university%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Education LIKE "%college%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Education LIKE "%certificate%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Education LIKE "%bootstrap%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Education LIKE "%cegep%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Education LIKE "%undergrad%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Education LIKE "%secondary school%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Education LIKE "%post-secondary%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Education LIKE "%post-secondary%";

SELECT COUNT(*) FROM skfrontendjobs
WHERE Education = "NA";

DELETE FROM abfrontendjobs
WHERE City = "Toronto, ON";
SELECT COUNT(*) FROM abfrontendjobs;