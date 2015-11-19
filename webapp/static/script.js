var app = angular.module("app", []);

var config = {
  api: 'http://localhost:5000'
};

var homeController = app.controller("HomeController", function($scope, DataService) {
  $scope.message = "foobar";
  $scope.repos = [];
  $scope.selectedRepos = [];
  $scope.featureSearchQuery = '';

  (function initialize() {
    DataService.getRepos().then(function(repos) {
      $scope.repos = repos;
    });
  })();

  $scope.submitForm = function() {
    console.log($scope.selectedRepos);
    console.log($scope.featureSearchQuery);
    DataService.getResults($scope.featureSearchQuery, $scope.selectedRepos);
  };

});

var dataService = app.service("DataService", function($http) {

  return {
    getRepos: function() {

      return $http.get(config.api + '/repos')
	.then(function(res) { 
	  // sort
	  res.data.sort(function(a,b) {
	    if(a.full_name > b.full_name) return 1;
            if(a.full_name < b.full_name) return -1;
	    return 0;
	  });
	  return res.data;
	});

    },
    searchFeatures: function() {

    },
    getResults: function(featureSearchQuery, selectedRepos) {
      $http.post(config.api + '/search', {
          query: featureSearchQuery,
          repos: selectedRepos
        }, {
	  headers: {
            "Content-Type": "application/json"
          }
        })
	.then(function(res) {
	  console.log(res);
	});
    }
  };

});
