# total score = sum(max scores for all)
# FINAL select hacker_id, name, total_score
# order by total score DESC, hacker_id ASC
# where total score is not 0

select hackers.hacker_id, hackers.name, scores.total_score

from hackers join

(select max_scores.hacker_id, sum(max_scores.max_score) as total_score from 

 (select submissions.hacker_id, max(submissions.score) as max_score from submissions group by hacker_id, challenge_id)
 as max_scores
 
group by max_scores.hacker_id) as scores

on hackers.hacker_id = scores.hacker_id



where scores.total_score != 0
order by scores.total_score desc, hackers.hacker_id
