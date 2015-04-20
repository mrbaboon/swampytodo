/**
 * Created by Alex on 4/19/2015.
 */
var ChatApp = angular.module('ChatApp', []);

//ChatApp.config(function($interpolateProvider, $httpProvider) {
//    $interpolateProvider.startSymbol('{$').endSymbol('$}');
//    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
//    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
//});

ChatApp.controller('ChatRoomCtrl', function($scope){

    $scope.messages = [
        {
            'sender': 'Alex',
            'message': 'Toot!'
        },
        {
            'sender': 'Seymore',
            'message': 'Thats rude!'
        }
    ];

});