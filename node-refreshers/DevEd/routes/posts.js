const express = require('express');
const router = express.Router();
const Post = require('../models/posts')

router.get('/', async (req,res) =>{
    try{
        const posts = await Post.find()
        res.send(posts)
    }catch(err){
        res.send({ message: err})
    }
})

router.post('/', (req,res) =>{    
    const post = new Post({
        title: req.body.title,
        description: req.body.description
    })

    post.save()
        .then(data => {
            res.send(data)
        })
        .catch(err => {
            res.json({ message: err })
        })

    // res.send('hello from posts')
})

router.get('/:postId', async (req,res) =>{
    try{
        const post = await Post.findById(req.params.postId)
        res.send(post)
    }catch(err){
        res.send({ message: err})
    }
})

router.delete('/:postId', async (req,res) =>{
    try{
        const post = await Post.remove({ _id: req.params.postId})
        res.send(post)
    }catch(err){
        res.send({ message: err})
    }
})

router.patch('/:postId', async (req,res) =>{
    try{
        const post = await Post.updateOne(
            { _id: req.params.postId },
            { $set: { title: req.body.title } }
        )
        res.send(post)
    }catch(err){
        res.send({ message: err})
    }
})

module.exports = router;