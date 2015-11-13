var app = angular.module("app", []),

config = {
  api: 'localhost:5000'
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


}),

dataService = app.service("DataService", function($http) {

  return {
    getRepos: function() {

      return $http.get(config.api + '/repos');

    },
    searchFeatures: function() {

    },
    getResults: function() {

    }
  };

});
