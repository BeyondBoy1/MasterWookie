/** CREATE
 * @param {Guild} [Guild] - The discord server you want to backup
 * @param {object} [options] - The backup options
 */

 const backup = require("discord-backup");
 backup.create(guild, {
    maxMessagesPerChannel: 10000,
    jsonSave: false,
    jsonBeautify: true,
    /* doNotBackup: [ "roles",  "channels", "emojis", "bans" ], */
 });

 /** LOAD 
  
 * @param {string} [backupID] - The ID of the backup that you want to load
 * @param {Guild} [Guild] - The discord server on which you want to load the backup
 */

backup.load(backupID, Guild).then(() => {
    backup.remove(backupID); // When the backup is loaded, it's recommended to delete it
});

/** FETCH INFO
 * @param {string} [backupID] - The ID of the backup to fetch
 */

 backup.fetch(backupID).then((backupInfos) => {
     console.log(backupInfos);
     /*
     {
         id: "BC5qo",
         size: 0.05
         data: {BackupData}
     }
     */
 });

 /**  REMOVE
 * @param {string} [backupID] - The ID of the backup to remove
 */

backup.remove(backupID);

/** LIST */
backup.list().then((backups) => {
    console.log(backups); // Expected Output [ "BC5qo", "Jdo91", ...]
});