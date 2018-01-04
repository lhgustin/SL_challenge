angular.module('SLApp')
    .config(['$locationProvider', '$routeProvider',
        function ($locationProvider,$routeProvider) {
                //  This prefix will appear in the links - good practice
                $locationProvider.hashPrefix('!');

                // ROUTES
                $routeProvider
                        .when('/',
                            {
                                // controller: 'SLController',
                                templateUrl: 'partials/landing.html'
                            })
                        .when('/app',
                            {
                                controller: 'SLController',
                                templateUrl: 'partials/app.html'
                            })
                        .otherwise({redirectTo:'/'});
}]);