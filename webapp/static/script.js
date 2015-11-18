var app = angular.module("app", []),

config = {
  api: 'http://localhost:5000'
},

homeController = app.controller("HomeController", function($scope, DataService) {
  $scope.message = "foobar";
  $scope.repos = [];

  (function initialize() {
    DataService.getRepos().then(function(repos) {
      $scope.repos = repos;
      console.log($scope.repos);
    });
  })();

  $scope.submitForm = function() {
    console.log('hello!');
  };

}),

dataService = app.service("DataService", function($http) {

  return {
    getRepos: function() {

      return $http.get(config.api + '/repos')
	.then(function(res) { 
	  // sort
/*	  res.data.sort(function(a,b) {
	    if(a.full_name > b.full_name) return 1;
            if(a.full_name < b.full_name) return -1;
	    return 0;
	  });*/
          console.log(res.data.length);
	  return res.data;
	});

    },
    searchFeatures: function() {

    },
    getResults: function() {

    }
  };

});
