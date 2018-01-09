angular.module('SLApp')
    .controller('AgencyCreatorCtrller', ['$scope', 'SLService','$location','$mdDialog', '$mdToast',
            function AgencyCreatorCtrller($scope, SLService, $location, $mdDialog, $mdToast) {
                    console.log('init AgencyCreatorCtrller');
                    $scope.gradeMapper = SLService.gradeMapper
                    $scope.gradeKeys = Object.keys($scope.gradeMapper)
                    $scope.addModel = {} // must be object first
                    $scope.addModel.grade = '0' // default, must be string as above

                     $scope.addAgency = function () {
                            $scope.serverErrors = false
                            var agencyJson = {
                                    'name' : $scope.addModel.name,
                                    'description' : $scope.addModel.description,
                                    'grade' : parseInt($scope.addModel.grade),
                                    'tags': $scope.addModel.tags}
                            SLService.addAgency(agencyJson)
                                .then(function success(result) {
                                        SLService.agencies.push(agencyJson)
                                        $mdDialog.hide()
                                        $mdToast.show(
                                              $mdToast.simple()
                                                .textContent('Agency created !')
                                                .position("top left")
                                                .hideDelay(250)
                                        );
                            }, function error(error) {
                                        console.log(error.statusText);
                                        $scope.serverErrors = true
                                        $scope.serverErrorsMsg = error.statusText
                            })
                    }

                    $scope.closeDialog = function () {
                            $mdDialog.hide();
                    }
            }]);