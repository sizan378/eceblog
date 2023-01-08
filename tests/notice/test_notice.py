
def test_notice(db, notice_factory):
    notice = notice_factory.create()
    # print("notice",notice.notice)
    assert notice.notice == notice.notice
