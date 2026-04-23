show dbs
use UFC2022
show collections

// 1. Count the total number of fighters in the Middleweight class
db.fighter_details.countDocuments({ weight_class: "Middleweight" })

// 2. Find unique stance values in the fighter_details collection
db.fighter_details.distinct("Stance")

// 3. Find fighters whose names start with the letter F
db.fighter.find({ fighter_name: /^F/ })

// 4. Find 5 events located in the USA
db.event.find({ location: /USA/ }).limit(5)

// 5. Find 5 fights where the Red corner won in the Lightweight class
db.ufc_fight.find({
  Winner: "Red",
  weight_class: "Lightweight"
}).limit(5)

// 6. Join fighter with fighter_details using Fighter_ID
db.fighter.aggregate([
  {
    $lookup: {
      from: "fighter_details",
      localField: "Fighter_ID",
      foreignField: "Fighter_ID",
      as: "fighter_details"
    }
  }
])

// 7. Join event with ufc_fight using Event_ID
db.event.aggregate([
  {
    $lookup: {
      from: "ufc_fight",
      localField: "Event_ID",
      foreignField: "Event_ID",
      as: "ufc_fights"
    }
  }
])