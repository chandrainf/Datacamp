'''
Sequencing stages


Here is a cursor, followed by four aggregation pipeline stages:

    cursor = (db.laureates.find(
        projection={"firstname": 1, "prizes.year": 1, "_id": 0},
        filter={"gender": "org"})
    .limit(3).sort("prizes.year", -1))

    project_stage = {"$project": {"firstname": 1, "prizes.year": 1, "_id": 0}}
    match_stage = {"$match": {"gender": "org"}}
    limit_stage = {"$limit": 3}
    sort_stage = {"$sort": {"prizes.year": -1}}

What sequence pipeline of the above four stages can produce a cursor db.laureates.aggregate(pipeline) equivalent to cursor above?

Instructions
50 XP

Possible Answers

    - [project_stage, match_stage, limit_stage, sort_stage]

    - [project_stage, match_stage, sort_stage, limit_stage]

    - [match_stage, project_stage, limit_stage, sort_stage]

    - [match_stage, project_stage, sort_stage, limit_stage]

Answer : [match_stage, project_stage, sort_stage, limit_stage]

'''
