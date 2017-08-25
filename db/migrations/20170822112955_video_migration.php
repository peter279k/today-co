<?php

use Phinx\Migration\AbstractMigration;

class VideoMigration extends AbstractMigration
{
    /**
     * Change Method.
     *
     * Write your reversible migrations using this method.
     *
     * More information on writing migrations is available here:
     * http://docs.phinx.org/en/latest/migrations.html#the-abstractmigration-class
     *
     * The following commands can be used in this method and Phinx will
     * automatically reverse them when rolling back:
     *
     *    createTable
     *    renameTable
     *    addColumn
     *    renameColumn
     *    addIndex
     *    addForeignKey
     *
     * Remember to call "create()" or "update()" and NOT "save()" when working
     * with the Table class.
     */
    private $tables = [
        'subscribers', 'porn_videos'
    ];

    public function change()
    {
        foreach($this->tables as $tableName) {
            $exists = $this->hasTable($tableName);
            if ($exists) {
                // do something if the current table existed
                $this->dropTable($tableName);
            }
        }
        $length10 = 10;
        $length50 = 50;
        $length6 = 6;
        // subscribers table
        $table = $this->table($this->tables[0], array('comment' => '訂閱者資料表', 'id' => false, 'primary_key' => array('id')));
        $table->addColumn('id', 'integer', array('limit' => MysqlAdapter::INT_MEDIUM, 'comment' => 'AUTO_INCREMENT'))
            ->addColumn('email', 'string', array('limit' => $length50, 'comment' => '信箱'))
            ->addColumn('verify', 'boolean', array('comment' => 'users whether has verified the email address'))
            ->addColumn('type', 'string', array('limit' => $length6, 'comment' => 'subscribe video is weekly or daily'))
            ->create();

        // porn_videos table
        $table = $this->table($this->table[1], array('comment' => 'porn video table', 'id' => false, 'primary_key' => array('id')));
        $table->addColumn('id', 'integer', array('limit' => MysqlAdapter::INT_MEDIUM, 'comment' => 'AUTO_INCREMENT'))
            ->addColumn('source', 'string', array('limit' => $length10, 'comment' => 'xvideo/avgle...'))
            ->addColumn('view_numbers', 'string', array('limit' => $length10, 'comment' => ''))
            ->addColumn('video_id', 'string', array('limit' => $length50, 'comment' => 'xvideo/avgle...'))
            ->addColumn('view_ratings', 'string', array('limit' => $length10, 'comment' => 'the video ratings'))
            ->addColumn('video_title', 'string', array('limit' => $length50, 'comment' => 'the video images title'))
            ->addColumn('create_date', 'date', array('comment' => 'the date of creating video'))
            ->create();
        // sites_url
        $table = $this->table($this->table[2])
    }
}
