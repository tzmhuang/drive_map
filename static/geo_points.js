// import pts_nusc from './nusc_data.json';// assert { type: 'json' };
// import pts_kitti from './kitti_data.json';// assert { type: 'json' };

// // export pts_nusc
// // console.log(pts_nusc)
// // module.exports = {pts_nusc};
// // var pts_nusc = nusc_data

// import pts_custom from './custom_data.json';// assert { type: 'json' };
// import pts_web from './youtube_data.json';// assert { type: 'json' };
// import pts_upload from './upload_data.json';// assert { type: 'json' };
// console.log(pts_upload)



const pts_nusc = require('./nusc_data.json');
const pts_kitti = require('./kitti_data.json');

const pts_custom = require('./custom_data.json');
const pts_web = require('./youtube_data.json');
const pts_upload = require('./upload_data.json');

export { pts_nusc, pts_kitti, pts_web, pts_custom, pts_upload };
