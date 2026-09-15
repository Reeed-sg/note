# yuri_mynote_app LOG

## 2026-09-11
- 何を：アプリ名を「YURIのマイノート帖」から「note壁打ちアプリ」に変更（app.py の page_title、template.html の title/h1見出し2箇所）。GitHub（Reeed-sg/note リポジトリ）にpushし、Streamlit Cloud（urerunote.streamlit.app）側にも反映。
- なぜ：経営者から前回作成した本アプリの名称変更依頼があったため。
- どうなったか：push完了、Streamlit Cloudが再デプロイされる想定。あわせて経営者から「合言葉(note2222)で入れない」「毎回起こす必要がある？」という問い合わせあり。合言葉のSHA-256ハッシュ照合ロジック自体は正しく"note2222"と一致することを確認済み（コード側のバグではない）。無料枠のStreamlit Community Cloudは一定期間アクセスがないとアプリがスリープし、手動でWake upが必要になる仕様のため、それが原因の可能性が高いと推測。今回のpushで再デプロイされるため解消される見込みだが、経営者に実際にアクセスできるか確認してもらう必要あり。
- 学び：同じコンセプトのアプリがClaude Artifact版（claude.ai上）とStreamlit版（GitHub連携・streamlit.app）の2箇所に存在していた。名称変更などの依頼時は「どちらのことか」を都度確認せず、両方の存在を意識して確認する。

## 2026-09-15
- なぜ：Hiromiさんより、実際に使ったユーザー（初回利用）からの6点のUXフィードバックを受領。全体像が見えない、冒頭の質問文言と選択肢がつながりにくい、有料/無料の判断材料がない、深掘り質問の意図が分かりにくい、コピー後の仕上げ方が分からない、書き方の使い分け目安がない、という指摘
- 何を：index.html（Claude Artifact版）とtemplate.html（Streamlit版）の両方に同一内容で6点を修正。①冒頭に「①書き方選択→②問いに答える→③AIで清書」の3ステップとできる範囲の説明を追加 ②welcome文言を「どんな気分で書きたい？」→「どちらの書き方で始める？」に変更 ③①のセクションに質問から書く/売れる型から書くの使い分け目安を追加 ④②のセクションに無料/有料記事の違いと「迷ったら無料のままでOK」を追加 ⑤深掘り質問「もう一場面」の説明を本文中での使い道が分かる表現に修正 ⑥フッター下に「コピーしたあと、どうする？」（AIへの渡し方・プロンプト例）を新設。編集後はPython html.parserでタグ対応・JSON構文を検証
- どうなったか：Hiromiさんの了承を得てClaude Artifact（https://claude.ai/artifact/5JeSzYgrTDGuR3tacPuKGa）を再公開（Version19）、GitHub（Reeed-sg/note）にpushしStreamlit Cloud側も再デプロイ
- 次やること：Hiromiさんに実際の画面を確認してもらい、追加の調整があれば反映する
