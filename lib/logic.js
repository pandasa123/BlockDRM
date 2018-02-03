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
 * Track the trade of a game from one trader to another
 * @param {org.acme.trading.Trade} trade - the trade to be processed
 * @transaction
 */
function tradeGame(trade) {

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
