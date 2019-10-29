from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class Submission(models.Model):
    song_name = models.CharField(max_length=50, verbose_name='歌曲名稱')
    song_singer = models.CharField(max_length=50, verbose_name='歌手')
    submitter = models.CharField(max_length=10, verbose_name='提交者')
    submitterID = models.CharField(max_length=9, verbose_name='提交者學號')
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name="提交時間")

    class Meta:
        verbose_name, verbose_name_plural = '報名資料', '報名資料'

    def youtube_url(self):
        url = "https://www.youtube.com/results?search_query="
        if self.song_singer != '':
            url = url + self.song_singer + '+'
        url += self.song_name
        return format_html(
            '<a href="%s" target="_blank">youtube</a>' % url
        )

    def __str__(self):
        return self.submitterID + '-' + self.submitter


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = [
        'submitterID', 'submitter', 'submit_time',
        'song_singer', 'song_name', 'youtube_url'
    ]
    search_fields = (
        'submitterID', 'submitter', 'submit_time', 'song_singer', 'song_name'
    )
    ordering = (
        'submit_time', 'submitterID', 'song_name'
    )
