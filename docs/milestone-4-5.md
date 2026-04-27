# Milestone 4 & 5

**Group No.:** 12  
**Student Name:** Hoang Nguyen

## Database Selection

The MongoDB database used in this project is `UFC2022`. The available collections are `event`, `fighter`, `fighter_details`, and `ufc_fight`.

```javascript
show dbs
use UFC2022
show collections
```

## Query Tasks

### 1. Count the total number of fighters in the Middleweight class

```javascript
db.fighter_details.countDocuments({ weight_class: "Middleweight" })
```

**Explanation:** This query counts how many documents in the `fighter_details` collection belong to the Middleweight class. It is useful for identifying how many fighters in the database are categorized under that division.

### 2. Find unique stance values in the fighter_details collection

```javascript
db.fighter_details.distinct("Stance")
```

**Explanation:** This query returns the distinct stance values stored in the `fighter_details` collection, such as Orthodox, Southpaw, Switch, and Open Stance. It helps summarize the variety of fighter styles in the dataset.

### 3. Find fighters whose names start with the letter F

```javascript
db.fighter.find({ fighter_name: /^F/ })
```

**Explanation:** This query searches the `fighter` collection for fighters whose names begin with the letter `F`. It demonstrates how regular expressions can be used in MongoDB searches.

### 4. Find 5 events located in the USA

```javascript
db.event.find({ location: /USA/ }).limit(5)
```

**Explanation:** This query returns five event documents where the location contains the text `USA`. It demonstrates filtering and limiting results in MongoDB.

### 5. Find 5 fights where the Red corner won in the Lightweight class

```javascript
db.ufc_fight.find({
  Winner: "Red",
  weight_class: "Lightweight"
}).limit(5)
```

**Explanation:** This query retrieves five fights from the `ufc_fight` collection where the Red corner won and the fight belongs to the Lightweight class. It shows how multiple conditions can be combined in one query.

### 6. Join fighter with fighter_details using Fighter_ID

```javascript
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
```

**Explanation:** This aggregation query uses `$lookup` to combine the `fighter` collection with the `fighter_details` collection through `Fighter_ID`. It allows general fighter information and detailed fighter attributes to be displayed together.

### 7. Join event with ufc_fight using Event_ID

```javascript
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
```

**Explanation:** This aggregation query uses `$lookup` to join the `event` collection with the `ufc_fight` collection through `Event_ID`. It helps show which fights belong to each event.

## Notes

The original milestone file contained inconsistent numbering, mixed field naming, and outdated MongoDB formatting. This cleaned version uses clearer wording and standard MongoDB query structure for presentation.