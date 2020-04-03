<?php

use Phinx\Migration\AbstractMigration;
use Phinx\Db\Adapter\MysqlAdapter;

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
    protected $tables = [
        'subscribers', 'porn_videos', 'sites_format'
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
        $length100 = 100;
        $length50 = 50;
        $length6 = 6;
        // Phinx automatically creates an auto-incrementing primary key column called id for every table.

        // subscribers table
        $tableName = 'subscribers';
        $table = $this->table($tableName, array('comment' => '訂閱者資料表'));
        $table->addColumn('email', 'string', array('limit' => $length50, 'comment' => '信箱'))
            ->addColumn('verify', 'boolean', array('comment' => 'users whether has verified the email address'))
            ->addColumn('type', 'string', array('limit' => $length6, 'comment' => 'subscribe video is weekly or daily'))
            ->addIndex(array('email'), array('unique' => true))
            ->create();

        // porn_videos table
        $tableName = 'porn_videos';
        $table = $this->table($tableName, array('comment' => 'porn video table'));
        $table->addColumn('source', 'string', array('limit' => $length10, 'comment' => 'xvideo/avgle...'))
            ->addColumn('view_numbers', 'integer', array('limit' => MysqlAdapter::INT_MEDIUM, 'comment' => ''))
            ->addColumn('video_id', 'string', array('limit' => $length50, 'comment' => 'xvideo/avgle...'))
            ->addColumn('view_ratings', 'string', array('limit' => $length10, 'comment' => 'the video ratings'))
            ->addColumn('video_title', 'string', array('limit' => $length50, 'comment' => 'the video images title'))
            ->addColumn('video_url', 'string', array('limit' => $length100, 'comment' => 'the video url'))
            ->addColumn('img_url', 'string', array('limit' => $length100, 'comment' => 'the video preview image url'))
            ->addColumn('create_date', 'date', array('comment' => 'the date of creating video'))
            ->addIndex(array('video_id'), array('unique' => true))
            ->create();
        // sites_format
        $table = $this->table($this->tables[2], array('comment' => 'sites format'));
        $table->addColumn('source', 'string', array('limit' => $length10, 'comment' => 'video source(avgle/xvideo)'))
            ->addColumn('video_url', 'string', array('limit' => $length100, 'comment' => 'www.xvideos.com/video{video_id}/{video_title}'))
            ->addColumn('video_images', 'string', array('limit' => $length100, 'comment' => 'img-egc.xvideos.com/videos/thumbs/{1}/{2}/{3}/{uid}/{uid_img}'))
            ->addIndex(array('video_url', 'video_images'), array('unique' => true))
            ->create();
        // insert the default sites format string
        $rows = [
            [
              'source'  => 'avgle',
              'video_url'  => 'https://avgle.com/video/{video_url}',
              'video_images'  => 'https://static-clst.avgle.com/videos/{img_url}'
            ],
            [
                'source'  => 'xvideo',
                'video_url'  => 'www.xvideos.com/video{video_id}/{video_title}',
                'video_images'  => 'img-egc.xvideos.com/videos/thumbs/{1}/{2}/{3}/{uid}/{uid_img}'
            ]
        ];
        // this is a handy shortcut
        $this->insert('sites_format', $rows);

    }
}
