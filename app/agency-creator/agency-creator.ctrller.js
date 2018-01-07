angular.module('SLApp')
    .controller('AgencyCreatorCtrller', ['$scope', 'SLService','$location','$mdDialog',
            function AgencyCreatorCtrller($scope, SLService, $location, $mdDialog) {
                    console.log('init AgencyCreatorCtrller');
                    $scope.gradeMapper = SLService.gradeMapper
                    $scope.gradeKeys = Object.keys($scope.gradeMapper)
                    $scope.addform = {} // must be object first
                    $scope.addform.grade = '0' // default, must be string as above

                     $scope.addAgency = function () {
                            var agencyJson = {
                                    'name' : $scope.addform.name,
                                    'description' : $scope.addform.description,
                                    'grade' : parseInt($scope.addform.grade),
                                    'tags': $scope.addform.tags}
                            SLService.addAgency(agencyJson)
                                .then(function success(result) {
                                        SLService.agencies.push(agencyJson)
                                        $mdDialog.hide()
                            }, function error(result) {
                                        $mdDialog.hide()
                            })
                    }

                    $scope.closeDialog = function () {
                            $mdDialog.hide();
                    }
            }]);