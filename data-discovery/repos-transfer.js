var mongo = require('promised-mongo');

var sourceDB = mongo('da0.eecs.utk.edu/test', ['repos']);
var targetDB = mongo('da0.eecs.utk.edu/ossfinder', ['repos']);

var minWatchers = 20,
	minForks = 20,
	skip = 0,
	limit = 100,
	query = {'watchers': {'$gt': minWatchers}, 'forks': {'$gt': minForks}};


find(query, skip, limit);

function find(query, skip, limit) {
	sourceDB.repos
	.find(query)
	.skip(skip)
	.limit(limit)
	.then(function(records) {
		console.log('records found: ', records.length);
		// If records are found, insert the records, call
		// the find() function recursively.
		if(records.length > 0) {
			update(records);
			find(query, skip + limit, limit);
		} 
		// If no records are found, close the connections
		// and return -- this will conclude the program.
		else {
			return;
		}
	});
}

function update(records) {
	records.forEach(function(record) {
		targetDB.repos.update({
				id: record.id
			}, record, {
				upsert: true
			})
		.then(function(record) {
			console.log('record inserted: ', record.id);
		});
	});
}
