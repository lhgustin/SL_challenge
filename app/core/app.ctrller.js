angular.module('SLApp')
    .controller('SLController', ['$scope', 'SLService','$location','$mdDialog', '$anchorScroll',
            function CoreController($scope, SLService, $location, $mdDialog, $anchorScroll) {
                    console.log('init SLController');

                    $scope.showPrompt = function() {
                            var confirmOptions = {
                                templateUrl:'./agency-creator/agency-creator.template.html',
                                clickOutsideToClose:true,
                            }
                            $mdDialog.show(confirmOptions)
                          };

                     $scope.scrollTop = function () {
                        $anchorScroll();
                      };
            }]);