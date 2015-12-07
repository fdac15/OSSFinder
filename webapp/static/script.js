var app = angular.module("app", []);

var config = {
  //api: 'http://localhost:5000'
  api: 'http://' + window.location.hostname + ':' + window.location.port
};

var homeController = app.controller("HomeController", function($scope, DataService) {
  $scope.message = "foobar";
  $scope.repos = [{ full_name: 'Loading repos...' }];
  $scope.selectedRepos = [];
  $scope.featureSearchQuery = '';
  $scope.featureSearchResults = [];
  $scope.recommendationSearchResults = [];

  (function initialize() {
    DataService.getRepos().then(function(repos) {
      $scope.repos = repos;
    });
  })();

  $scope.selectRepo = function(item) {
    item = JSON.stringify(item);
    $scope.selectedRepos.push(JSON.parse(item));
  };

  $scope.deselectRepo = function(index) {
    $scope.selectedRepos.splice(index, 1);
  };

  $scope.submitFeatureSearch = function() {
    DataService.featureSearch($scope.featureSearchQuery)
	.then(function(results) {
          $scope.featureSearchResults = results;
        });
  };

  $scope.submitRecommendationSearch = function() {
    console.log($scope.selectedRepos);
    console.log($scope.featureSearchQuery);
    DataService.recommendationSearch($scope.featureSearchQuery, $scope.selectedRepos)
	.then(function(results) {
          $scope.recommendationSearchResults = results;
	});
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
    featureSearch: function(featureSearchQuery) {
      return $http.post(config.api + '/search/feature', {
        query: featureSearchQuery
      }, {
        headers: {
          "Content-Type": "application/json"
        }
      })
      .then(function(res) {
         return res.data;
      });
    },
    recommendationSearch: function(featureSearchQuery, selectedRepos) {
      return $http.post(config.api + '/search/recommendation', {
          query: featureSearchQuery,
          repos: selectedRepos
        }, {
	  headers: {
            "Content-Type": "application/json"
          }
        })
	.then(function(res) {
	  return res.data;
	});
    }
  };

});
