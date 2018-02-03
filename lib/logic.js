/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Track the trade of a game from one user to another
 * @param {org.acme.trading.Trade} trade - the trade to be processed
 * @transaction
 */
function buySellGame(trade) { // New key needed 

    // set the new owner of the game
    trade.game.owner = trade.newOwner;
    return getAssetRegistry('org.acme.trading.Game')
        .then(function (assetRegistry) {

            // emit a notification that a trade has occurred
            var tradeNotification = getFactory().newEvent('org.acme.trading', 'TradeNotification');
            tradeNotification.game = trade.game; // Check if these lines work
      		trade.game.gameKey = generateKey(trade.game.gameName); // Check if these lines work
            emit(tradeNotification);

            // persist the state of the game
            return assetRegistry.update(trade.game);
        });
}

function giftGame(trade) {

    // set the new owner of the game
    trade.game.owner = trade.newOwner;
    return getAssetRegistry('org.acme.trading.Game')
        .then(function (assetRegistry) {

            // emit a notification that a trade has occurred
            var tradeNotification = getFactory().newEvent('org.acme.trading', 'TradeNotification');
            tradeNotification.game = trade.game;
            emit(tradeNotification);

            // persist the state of the game
            return assetRegistry.update(trade.game);
        });
}

/**
 * Returns a random integer between min (inclusive) and max (inclusive)
 * Using Math.round() will give you a non-uniform distribution!
 */
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

/**
 * Generates and returns a random 30-digit key
 */
function generateKey(gameName) {
    var key = "";
    for (var i = 0; i < 30; i++) {
        key = key + String(getRandomInt(0,9));
    }
    return key;
}

/**
 * Remove all high volume Games
 * @param {org.acme.trading.RemoveHighQuantityGames} remove - the remove to be processed
 * @transaction
 */
function removeHighQuantityGames(remove) {

    return getAssetRegistry('org.acme.trading.Game')
        .then(function (assetRegistry) {
            return query('selectGamesWithHighQuantity')
                    .then(function (results) {

                        var promises = [];

                        for (var n = 0; n < results.length; n++) {
                            var trade = results[n];

                            // emit a notification that a trade was removed
                            var removeNotification = getFactory().newEvent('org.acme.trading', 'RemoveNotification');
                            removeNotification.game = trade;
                            emit(removeNotification);

                            // remove the game
                            promises.push(assetRegistry.remove(trade));
                        }

                        // we have to return all the promises
                        return Promise.all(promises);
                    });
        });
}