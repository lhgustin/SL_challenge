angular.module('SLApp')
    .controller('AgencyListCtrller', ['$scope', 'SLService','$location',
            function AgencyListCtrller($scope, SLService, $location) {
                    console.log('init AgencyListCtrller');

                    $scope.gradeMapper = {
                            '0':'PADAWAN',
                            '1':'JEDI',
                            '2':'MASTER'
                    }

                    /* INIT calls of this controller */
                    SLService.getAgencies().then(
                        function (result) {
                                $scope.agencies = result;
                                console.log("Agencies loaded "+$scope.agencies.length)
                        },
                        function(error) {
                                console.log(error.statusText);
                        }
                    )
            }]);