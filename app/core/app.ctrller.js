angular.module('SLApp')
    .controller('SLController', ['$scope', 'SLService','$location','$mdDialog', '$anchorScroll','$mdSidenav',
            function CoreController($scope, SLService, $location, $mdDialog, $anchorScroll, $mdSidenav) {
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

                     /**
                   * Hide or Show the 'left' sideNav area
                   */
                  $scope.toggleList = function () {
                    $mdSidenav('right').toggle();
                  }
            }]);