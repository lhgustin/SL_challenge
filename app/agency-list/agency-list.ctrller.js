angular.module('SLApp')
    .controller('AgencyListCtrller', ['$scope', 'SLService','$location',
            function AgencyListCtrller($scope, SLService, $location) {
                    console.log('init AgencyListCtrller');

                    $scope.gradeMapper = SLService.gradeMapper
                    $scope.gradeColorMapper = SLService.gradeColorMapper


                    /* INIT calls of this controller */
                    SLService.getAgencies().then(
                        function (result) {
                                SLService.agencies = result
                                $scope.agencies = SLService.agencies;
                                console.log("Agencies loaded "+$scope.agencies.length)
                        },
                        function(error) {
                                console.log(error.statusText);
                                $scope.serverErrors = true
                                $scope.serverErrorsMsg = error.statusText
                        }
                    )
            }]);